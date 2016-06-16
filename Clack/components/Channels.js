var React = require('react');
var ReactDOM = require('react-dom');

var Channels = React.createClass({
  render: function() {
    var channelList = this.props.channels.map(function(channel, i) {
      return (
        <li key={i} className="channel active">
          <a className="channel_name">
            <span className="unread">0</span>
            <span><span className="prefix">#</span>{channel}</span>
          </a>
        </li>
      )
    })

      <div className="listings_channels">
        <h2 className="listings_header">Channels</h2>
        <ul className="channel_list">
          {channelList}
        </ul>
      </div>
      <div className="listings_direct-messages"></div>

    )
  }
})

module.exports = Channels;
